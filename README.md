# NASA Space Biology Knowledge Engine - Scraping Tools

## Project Overview

This repository contains automated web scraping tools developed for the **NASA Space Apps Challenge 2025** - specifically addressing the challenge: **Build a Space Biology Knowledge Engine**.

The goal of this project is to build intelligent tools that can automatically collect, organize, and structure research papers from NASA's space biology databases. These tools help create a comprehensive knowledge base of space biology research that can power AI-driven knowledge engines and facilitate scientific discovery.

## Challenge Context: Build a Space Biology Knowledge Engine

The NASA Space Apps Challenge called for innovative solutions to aggregate and organize the vast amount of space biology research scattered across various databases. Space biology research is critical for:

- Understanding how living organisms respond to space environments
- Developing countermeasures for long-duration space missions
- Supporting future lunar and Martian exploration
- Advancing biological sciences through unique microgravity experiments

However, this valuable research is often siloed in different databases, making it difficult for researchers, students, and the public to access and utilize this information effectively.

### Our Solution

This repository provides automated scraping tools that:

1. **Systematically collect** space biology publications from NASA databases
2. **Extract metadata** including titles, authors, abstracts, and publication details
3. **Download full-text PDFs** for comprehensive analysis
4. **Structure data** in CSV format for easy integration with knowledge engines
5. **Enable scalable collection** of research papers for building comprehensive databases

## Repository Contents

### 1. `100_pdfs_nasa.py`

**Purpose**: Automated web scraper for collecting NASA space biology research papers

**Key Features**:
- Scrapes NASA's Life Sciences Data Archive (LSDA) and related databases
- Extracts comprehensive metadata from publication pages
- Downloads full-text PDFs automatically
- Implements smart navigation through search results and pagination
- Includes error handling and retry logic for robust data collection
- Uses Selenium WebDriver for dynamic content handling

**Capabilities**:
- Collects up to 100+ research papers per execution
- Extracts: titles, authors, abstracts, publication dates, DOIs, PMC IDs
- Saves metadata to structured CSV files
- Organizes downloaded PDFs in designated folders
- Handles various NASA database interfaces and formats

### 2. `SB_publication_PMC.csv`

**Purpose**: Sample dataset of space biology publications with PubMed Central identifiers

**Structure**:
- Contains metadata for space biology research papers
- Includes PMC IDs for direct access to full-text articles
- Fields include: publication titles, authors, journals, dates, identifiers
- Serves as reference data for training and testing knowledge engines

**Use Cases**:
- Training dataset for machine learning models
- Reference list for validation and verification
- Quick access index to key space biology publications
- Starting point for expanding the knowledge base

### 3. `msedgedriver`

**Purpose**: Microsoft Edge WebDriver executable for Selenium automation

**Function**:
- Enables automated browser control for web scraping
- Required dependency for running the scraping scripts
- Platform-specific binary for browser automation
- Compatible with Selenium WebDriver API

## Technical Setup

### Prerequisites

```bash
# Required Python packages
pip install selenium
pip install pandas
pip install requests
pip install beautifulsoup4
```

### Environment Requirements

- **Python**: 3.7 or higher
- **Browser**: Microsoft Edge (or Chrome with appropriate driver)
- **Operating System**: Windows, macOS, or Linux
- **Internet**: Stable connection for accessing NASA databases

### Configuration

1. Ensure `msedgedriver` is executable:
   ```bash
   chmod +x msedgedriver  # Unix/Linux/macOS
   ```

2. Place the driver in your system PATH or specify its location in the script

3. Configure scraping parameters in `100_pdfs_nasa.py`:
   - Set target number of papers
   - Specify output directories
   - Adjust wait times and timeouts

### Running the Scraper

```bash
python 100_pdfs_nasa.py
```

The script will:
1. Initialize the web driver
2. Navigate to NASA space biology databases
3. Search for relevant publications
4. Extract metadata from each result
5. Download available PDFs
6. Save all data to CSV file
7. Generate summary report

## Ideal Use Cases

### 1. Building AI Knowledge Engines
- **Purpose**: Create comprehensive databases for RAG (Retrieval-Augmented Generation) systems
- **Application**: Feed collected papers into LLMs for question-answering about space biology
- **Benefit**: Enable natural language queries about space biology research

### 2. Research Meta-Analysis
- **Purpose**: Aggregate publications for systematic reviews
- **Application**: Analyze trends, methodologies, and findings across multiple studies
- **Benefit**: Identify research gaps and opportunities

### 3. Educational Resources
- **Purpose**: Build curated collections for students and educators
- **Application**: Create searchable databases of space biology educational materials
- **Benefit**: Make space biology research accessible to broader audiences

### 4. Literature Discovery
- **Purpose**: Help researchers find relevant papers quickly
- **Application**: Power recommendation systems for related research
- **Benefit**: Accelerate scientific discovery through better information access

### 5. Data Science Projects
- **Purpose**: Provide datasets for NLP and machine learning experiments
- **Application**: Text mining, topic modeling, citation analysis
- **Benefit**: Enable computational analysis of space biology literature

### 6. Knowledge Graph Construction
- **Purpose**: Extract entities and relationships from research papers
- **Application**: Build interconnected knowledge graphs of space biology concepts
- **Benefit**: Visualize connections between research areas, methods, and findings

## Data Output Format

The scraper generates CSV files with the following structure:

| Field | Description |
|-------|-------------|
| Title | Publication title |
| Authors | List of authors |
| Abstract | Paper abstract/summary |
| Publication Date | Date of publication |
| Journal | Journal or publication venue |
| DOI | Digital Object Identifier |
| PMC ID | PubMed Central ID |
| PDF URL | Link to full-text PDF |
| Keywords | Research keywords/tags |

## Ethical Considerations

- **Respect robots.txt**: The scraper follows website guidelines
- **Rate limiting**: Implements delays to avoid overloading servers
- **Terms of service**: Designed for use with publicly accessible NASA data
- **Attribution**: All collected data maintains proper citation information
- **Fair use**: Intended for research, education, and non-commercial purposes

## Future Enhancements

- [ ] Support for additional NASA databases
- [ ] Multi-threaded scraping for faster collection
- [ ] Natural language processing for automatic paper summarization
- [ ] Integration with knowledge graph databases (Neo4j, etc.)
- [ ] API wrapper for programmatic access
- [ ] Docker containerization for easy deployment
- [ ] Cloud storage integration (AWS S3, Google Cloud Storage)
- [ ] Real-time monitoring and alerting for new publications

## Contributing

This project was developed for the NASA Space Apps Challenge 2025. Contributions, suggestions, and improvements are welcome!

## License

This project is developed for educational and research purposes as part of the NASA Space Apps Challenge.

## Acknowledgments

- **NASA Space Apps Challenge 2025** for inspiring this project
- **NASA Life Sciences Data Archive** for providing open access to space biology research
- **PubMed Central** for hosting full-text scientific articles
- The space biology research community for their invaluable contributions to science

## Contact

For questions, suggestions, or collaboration opportunities related to this NASA Space Apps Challenge project, please open an issue in this repository.

---

**Built for NASA Space Apps Challenge 2025 - Build a Space Biology Knowledge Engine**
