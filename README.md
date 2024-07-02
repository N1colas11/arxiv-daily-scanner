# ArXiv Daily Scanner

This project fetches and displays papers submitted to arXiv on the previous day.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/arxiv-daily-scanner.git
   cd arxiv-daily-scanner
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Ensure your virtual environment is activated, then run the script with:

```
python src/arxiv_scanner.py
```

This will fetch papers submitted to arXiv on the previous day and display their titles, authors, and summaries.

## Running Tests

To run the unit tests:

```
python -m unittest discover tests
```

## Deactivating the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment:

```
deactivate
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.