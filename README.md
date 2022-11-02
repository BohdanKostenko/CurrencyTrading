# Currency Trading
___

Given a matrix of currency pair exchange rates, a Python 3.10 algorithm is built that either finds a profitable risk-free trading strategy and presents it,
or prints "no risk-free opportunities" in case there is no profitable risk-free currency trading strategy.

To run the script, use the command in terminal:

    $ python trading.py PATH
    
Where `PATH` is the path to your .csv file

## Example
____

### Input

Matrix of n currency exchange rates similar to:

|        | Curr.1 | Curr.2 | Curr.3 |
|-------:|:------:|:------:|:-------|
| Curr.1 |  1.00  |  1.20  | 0.89   |
| Curr.2 |  0.88  |  1.00  | 5.10   |
| Curr.3 |  1.10  |  0.15  | 1.00   |
                                            

  *Example file currency_matrix.csv*

    ,Curr.1,Curr.2,Curr.3
    Curr.1,1.00,1.20,0.89
    Curr.2,0.88,1.00,5.10
    Curr.3,1.10,0.15,1.00                       


### Output

    Curr.1 Curr.2 Curr.1 conversion rate 5.6

## Docker
___

Install Docker 

 https://docs.docker.com/desktop/

To create an image from a Dockerfile, you need to run:

    $ docker build . --tag trading
                                          
you only need to specify the directory in which this file is located (and . means that the file is located in the 
directory from which the console was launched)

Now, let's run the container from our image with the docker run pyramid command:

    $ docker run -v PATH:/matrix:ro -it trading /matrix

Where `PATH` is the path to your .csv file in local host