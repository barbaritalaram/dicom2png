# 🏥 DICOM to PNG Converter

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/barbaritalaram/dicom2png/blob/main/LICENSE)

A simple and efficient Python script to convert DICOM medical images to PNG format while maintaining image quality. This tool is particularly useful for medical imaging professionals and researchers who need to convert DICOM files to a more widely compatible format.

## ✨ Features

- 🔄 Converts DICOM files to high-quality PNG images
- 📁 Supports batch processing of multiple files
- 🗂️ Preserves original directory structure
- 🛡️ Handles DICOM files with or without extensions
- 📊 Provides progress feedback during conversion
- ⚡ Fast and efficient processing

## 📋 Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/barbaritalaram/dicom2png.git
cd dicom2png
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

The script can be used from the command line with two required arguments:

```bash
python dicom2png.py input_directory output_directory
```

### Example:
```bash
python dicom2png.py ./dicom_images ./png_output
```

### Arguments:
- `input_directory`: Path to the folder containing DICOM files
- `output_directory`: Path where the converted PNG files will be saved

## 📁 Directory Structure

```
dicom2png/
│
├── dicom2png.py      # Main conversion script
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## 🔧 How It Works

1. The script scans the input directory for DICOM files
2. Each DICOM file is read and converted to a PNG image
3. The original directory structure is maintained in the output folder
4. Progress is displayed in the console during conversion

## ⚠️ Error Handling

- The script handles errors gracefully and continues processing even if one file fails
- Error messages are displayed for any files that fail to convert
- The script creates necessary output directories automatically

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/barbaritalaram/dicom2png/blob/main/LICENSE) file for details.

## 🙏 Acknowledgments

- [pydicom](https://github.com/pydicom/pydicom) - For DICOM file handling
- [Pillow](https://github.com/python-pillow/Pillow) - For image processing

## 📧 Contact

Barbarita Lara - [@barbaritalaram](https://github.com/barbaritalaram)

Project Link: [https://github.com/barbaritalaram/dicom2png](https://github.com/barbaritalaram/dicom2png) 
