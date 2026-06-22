# Needleman–Wunsch Sequence Alignment Web Application

A Flask-based web application implementing the Needleman–Wunsch algorithm for global sequence alignment. The application allows users to align biological sequences using customizable scoring parameters and visualize the dynamic programming scoring matrix.

---

## Features

- Global sequence alignment using the Needleman–Wunsch algorithm
- Adjustable match, mismatch, and gap scores
- Dynamic programming scoring matrix visualization
- Traceback to obtain the optimal alignment
- Alignment statistics
  - Alignment Score
  - Number of Matches
  - Number of Mismatches
  - Number of Gaps
  - Identity Percentage
- Input validation with user-friendly error messages
- Clean and responsive web interface built with Flask

---

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Dynamic Programming
- Bioinformatics Algorithms

---

## Project Structure

```
needleman-wunsch/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── results.html
│   └── error.html
│
├── static/
│   └── DNA.json
├──videos
|   └── sample.gif
├──requirements.txt
README.md
```

---

## Project Demo

[▶ Watch Demo](needleman-wunsch/videos/sample.gif)


## Installation

Clone the repository

```bash
git clone https://github.com/veenaaa02/Needleman-Wunsch.git
```

Move into the project

```bash
cd needleman-wunsch
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## How It Works

1. Enter two biological sequences.
2. Specify match, mismatch, and gap scores.
3. Submit the form.
4. The application computes the dynamic programming matrix.
5. Traceback is performed to determine the optimal global alignment.
6. Results and alignment statistics are displayed.

---

## Example Output

**Input**

Sequence 1

```
GATTACA
```

Sequence 2

```
GCATGCU
```

The application displays

- Optimal alignment
- Alignment score
- Dynamic programming matrix
- Match count
- Mismatch count
- Gap count
- Identity percentage

---

## Time Complexity

- Time Complexity: **O(m × n)**
- Space Complexity: **O(m × n)**

where **m** and **n** are the lengths of the input sequences.

---

## Author

**Veena G**

Bioinformatics | Python | Flask | Algorithms
