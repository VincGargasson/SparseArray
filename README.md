# SparseArray

SparseArray is a Python class that determines for a given collection of queries strings, the number of time each element of this collection occurs in the following list : `['ab','abc','abc','abc','bc','bc']`. 
 The result is given in a dictionnary.


Example: 
```python
queries strings = ['ab','bc']
returned result = {'ab': 1, 'bc': 2}
```

## Installation

Clone this repo on your local computer
```bash
git clone git@github.com:VincGargasson/SparseArray.git
```


#### Send request with your terminal

If you want to get access to the script localy with your terminal, write the following in your terminal :


```bash
#Go to the SparseArray directory
cd Local_SparseArray/
#Build the docker image
docker build -t test_mdm .
#Run the container on your localhost
docker run -t test_mdm your_query_strings
```

#### Send request through the API

If you want to get access to the script localy with an API UI, write the following in your terminal :

```bash
#Go to the SparseArray directory
cd API_SparseArray/
#Build the docker image
docker build -t test_mdm .
#Run the container on your localhost
docker run -it -p 5000:5000 test_mdm
```
And then access your result on [here](http://0.0.0.0:5000/docs.html)

### Have fun 8-)
