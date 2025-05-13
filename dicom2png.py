import os
import pydicom
from PIL import Image
import argparse

def is_dicom_file(file_path):
    """
    Check if a file is a DICOM file by trying to read it
    """
    try:
        pydicom.dcmread(file_path)
        return True
    except:
        return False

def convert_dicom_to_png(dicom_path, output_path):
    """
    Convert a DICOM file to PNG format while maintaining quality
    """
    try:
        # Read the DICOM file
        dicom_data = pydicom.dcmread(dicom_path)
        
        # Get the pixel data
        pixel_array = dicom_data.pixel_array
        
        # Convert to PIL Image
        image = Image.fromarray(pixel_array)
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Save as PNG with maximum quality
        image.save(output_path, 'PNG', quality=100)
        print(f"Successfully converted: {dicom_path} -> {output_path}")
        
    except Exception as e:
        print(f"Error converting {dicom_path}: {str(e)}")

def process_directory(input_dir, output_dir):
    """
    Process all DICOM files in a directory and its subdirectories
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Walk through the input directory
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            # Check if file is a DICOM file (with or without extension)
            file_path = os.path.join(root, file)
            if is_dicom_file(file_path):
                # Create corresponding output path
                rel_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, rel_path)
                output_path = os.path.join(output_subdir, f"{file}.png")
                
                # Convert the file
                convert_dicom_to_png(file_path, output_path)

def main():
    parser = argparse.ArgumentParser(description='Convert DICOM files to PNG format')
    parser.add_argument('input_dir', help='Input directory containing DICOM files')
    parser.add_argument('output_dir', help='Output directory for PNG files')
    
    args = parser.parse_args()
    
    print(f"Starting conversion from {args.input_dir} to {args.output_dir}")
    process_directory(args.input_dir, args.output_dir)
    print("Conversion completed!")

if __name__ == "__main__":
    main() 