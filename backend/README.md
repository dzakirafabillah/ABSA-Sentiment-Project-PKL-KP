# Backend for ABSA Sentiment Project

## Getting Started

This will give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Installation

#### Prerequisites
* python 3.7.6

#### Set Up
1. Clone repository.
```sh
    git clone https://github.com/dzakirafabillah/ABSA-Sentiment-Project-PKL-KP
```
2. Masuk ke folder backend
```sh
    cd backend
```
3. Clone https://github.com/1tangerine1day/Aspect-Term-Extraction-and-Analysis.git kemudian rename menjadi ABSA_SentimentMultiEmiten dan simpan dalam folder backend.
4. Download model hasil training dan simpan di dalam folder models 
5. Jalankan command 
    `pip install -r requirements.txt`

#### Menjalanan API
1. Build API 
    `uvicorn app:app --reload`

Struktur Folder :
-
![image](https://user-images.githubusercontent.com/61398214/186295869-4f9ac588-eb67-48aa-bada-b88d325abe8d.png)
