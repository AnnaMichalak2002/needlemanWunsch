## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project has been created to complete 'Assignment 2 - Sequence Alignment' laboratory.
	
## Technologies
Project is created with:
* Python version: 3.12.0
	
## Setup
To run this project, ensure that you have Python 3.12.0 installed on your system.

1. **Install Python 3.12.0**: If you don't have Python 3.12.0 installed, you can download it from the official Python website [here](https://www.python.org/downloads/release/python-3120/).

2. **Clone the Repository**: If you haven't already, clone this project's repository to your local machine.

    ```bash
    git clone https://github.com/AnnaMichalak2002/needlemanWunsch.git
    ```

3. **Navigate to the Project Directory**: Use your terminal to navigate to the project directory.

    ```bash
    cd needlemanWunsch
    ```

4. **Run the Script**: To execute the main script, type the following command:

    ```bash
    python script.py example.fasta
    ```
    or
    ```bash
    python script.py example2.fasta
    ```

5. **Expected output**:

    ```bash
	Alignment 1: MVLSEGEWQLVLHVWAKVEADVAGHGQDIFIRLFKSHPETLEKFDRFKHLKTEAEMKASEDLKKQGVTVLTALGAILKKKGHHEAELKPLAQSHATKHKIPIKYLEFISEAIIHVLHSRHPGDFGADAQGAMNKALELFRKDIAAKYKELGYQG
	Alignment 2: -GLSDGEWQLVLNVWGKVEADVAGHGQEVLIRLFKGHPETLEKFDKFKHLKSEDEMKASEDLKKVGNTILTALGGILKKKGHHEAELTPLAQSHATKHKIPVKYLEFISEAIIQVLQSKHPGDFGADAQGAMSKALELFRNDMAAKYKELGFQG
	Score: 103
    ```
    or

    ```bash
	Alignment 1: -GLSDGEWQLVLNVWGKVEADVAGHGQEVLIRLFKGHPETLEKFDKFKHLKSEDEMKASEDLKKVGNTILTAL---GGILKKKGHHEAELTPLAQSHATKHKIPVKYLEFISEAIIQVLQSKHPGDFGADAQGAMSKALELFRNDMAAKYKELGFQG
	Alignment 2: XSLSAAEADLAGKSWAPVFANKNANGLDFLVALFEKFPDSANFFADFK-GKSVADIKASPKLRDVSSRIFTRLNEFVNNAANAGKMSAMLSQFAKEHVGFGVGSAQFENVRSMFPGFV-ASVAAPPAGADA--AWTK---LFGLIIDA-LKAAG--A
	Score: -83
    ```

