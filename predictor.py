#!/usr/bin/python

import argparse
import naiveBayes as nb

parser = argparse.ArgumentParser()

#add command --train
parser.add_argument(
                '--train',
                nargs='*',
                required=True,
                help='A list of csv files containing training data')

#add command --test to assign testing dataset
parser.add_argument(
                '--test',
                required=True,
                help='A csv file containing testing data')

#add --result to assign result file name
parser.add_argument('--result', help='assign name to the result file in .csv')
args = parser.parse_args()

trainingData = args.train
testingData = args.test
resultFile = args.result

predictor = nb.pubgNaiveBayes(trainingData)
predictor.classify_data(testingData, resultFile)