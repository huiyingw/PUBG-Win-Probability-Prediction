import csv

attributes = ['solo_KillDeathRatio', 'solo_DamagePg', 'solo_AvgSurvivalTime', 'solo_WinRatio']
num_attribute_values = {
    'solo_KillDeathRatio': 8,
    'solo_DamagePg': 12,
    'solo_AvgSurvivalTime': 7,
    'solo_WinRatio': 9,

}
#classes
winRatioRange = ['<=5', '(5, 10]', '(10, 15]', '(15, 20]', '(20, 25]', '(25, 30]', '(30, 35]', '(35, 50]', '>=50']

class pubgNaiveBayes:

    #Initilizes the instance
    #trainingData could be several csv files
    def __init__(self, trainingData):
        self.trainingDataaaa = []
        for trainingFile in trainingData:
            data = self.getCsv(trainingFile)
            dataMet = self.reArrangeData(data)
            self.trainingDataaaa.extend(dataMet)

    def classify_data(self, testData, result_file_name=None):
        #testData is the dataset to be analyzed
        
        #re-arrange the dataset into different ranges instead of just numbers
        testDataaaa = self.reArrangeData(self.getCsv(testData))
        #release to test result of re-arrangement data
        #result = self.writeCsv(testDataaaa, result_file_name)
        
        #Set up the list of results
        results = [['player']]
        results[0].extend(winRatioRange)
        results[0].append('class')

        # Classify test data and determine classification accuracy
        isMatching = 0
        for instance in testDataaaa:
            #find probabilities of the class given evidence except for the last one(winRatio, which is what we want to predict)
            probabilities = self.findProbClassGivenEvidence(instance[:-1])

            #update highest probability, and put the data into result
            all_probs = [instance[0]]
            highestP = 0
            classification = ''
            for val in winRatioRange:
                if probabilities[val] > highestP:
                    highestP = probabilities[val]
                    classification = val
                all_probs.append(probabilities[val])

            if classification == instance[-1]:
                isMatching += 1

            all_probs.append(classification)
            results.append(all_probs)

        #calculate accuracy
        accuracy = float(isMatching)/len(testDataaaa)
        results.append(['accuracy', accuracy])

        #write the results as .csv
        result_csv = self.writeCsv(results, result_file_name)

    def getCsv(self, data_file):
        with open(data_file, 'rb') as f:
            reader = csv.reader(f)
            return list(reader)

    def writeCsv(self, data, file_name):
        if file_name is None:
            file_name = 'result.csv'
        with open(file_name, 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(data)

    def reArrangeData(self, data):
        player_index = data[0].index('player_name')
        killDeathRatio_index = data[0].index('solo_KillDeathRatio')
        damagePg_index = data[0].index('solo_DamagePg')
        AvgSurvivalTime_index = data[0].index('solo_AvgSurvivalTime')
        winRatio_index = data[0].index('solo_WinRatio')


        processed_data = []
        for instance in data[1:]:
            # Replace values with threshold values
            # Transform killDeathRatio
            killDeathRatio_val = float(instance[killDeathRatio_index])
            if killDeathRatio_val <= 1.75:
                killDeathRatio = '<=1.75'
            elif 1.75 < killDeathRatio_val <= 3.5:
                killDeathRatio = '(1.75, 3.5]'
            elif 3.5 < killDeathRatio_val <= 5.25:
                killDeathRatio = '(3.5, 5.25]'
            elif 5.25 < killDeathRatio_val <= 7:
                killDeathRatio = '(5.25, 7]'
            elif 7 < killDeathRatio_val <= 8.75:
                killDeathRatio = '(7, 8.75]'
            elif 8.75 < killDeathRatio_val <= 10.5:
                killDeathRatio = '(8.75, 10.5]'
            elif 10.5 < killDeathRatio_val <= 15:
                killDeathRatio = '(10.5, 15]'                                
            elif 15 < killDeathRatio_val:
                killDeathRatio = '>=15'

            # winRatio
            winRatio_val = float(instance[winRatio_index])
            if winRatio_val <= 5:
                winRatio = '<=5'
            elif 5 < winRatio_val <= 10:
                winRatio = '(5, 10]'
            elif 10 < winRatio_val <= 15:
                winRatio = '(10, 15]'
            elif 15 < winRatio_val <= 20:
                winRatio = '(15, 20]'                
            elif 20 < winRatio_val <= 25:
                winRatio = '(20, 25]'
            elif 25 < winRatio_val <= 30:
                winRatio = '(25, 30]'
            elif 30 < winRatio_val <= 35:
                winRatio = '(30, 35]'
            elif 35 < winRatio_val <= 50:
                winRatio = '(35, 50]'
            elif 35 < winRatio_val:
                winRatio = '>=35'

            # damagePg
            damagePg_val = float(instance[damagePg_index])
            if damagePg_val <= 100:
                damagePg = '<=100'
            elif 100 < damagePg_val <= 200:
                damagePg = '(100, 200]'
            elif 200 < damagePg_val <= 300:
                damagePg = '(200, 300]'
            elif 300< damagePg_val <= 400:
                damagePg = '(300, 400]'
            elif 400 < damagePg_val <= 500:
                damagePg = '(400, 500]'
            elif 500 < damagePg_val <= 600:
                damagePg = '(500, 600]'
            elif 600 < damagePg_val <= 700:
                damagePg = '(600, 700]'
            elif 700 < damagePg_val <= 800:
                damagePg = '(700, 800]'
            elif 800 < damagePg_val <= 900:
                damagePg = '(800, 900]'
            elif 900 < damagePg_val <= 1000:
                damagePg = '(900, 1000]'
            elif 1000 < damagePg_val <= 1100:
                damagePg = '(1000, 1100]'
            elif 1100 < damagePg_val:
                damagePg = '>=1100'

            # AvgSurvivalTime
            AvgSurvivalTime_val = float(instance[AvgSurvivalTime_index])
            if AvgSurvivalTime_val <= 900:
                AvgSurvivalTime = '<=880'
            elif 900 < AvgSurvivalTime_val <= 1000:
                AvgSurvivalTime = '(900, 1000]'
            elif 1000 < AvgSurvivalTime_val <= 1100:
                AvgSurvivalTime = '(1000, 1100]'
            elif 1100 < AvgSurvivalTime_val <= 1200:
                AvgSurvivalTime = '(1100, 1200]'
            elif 1200 < AvgSurvivalTime_val <= 1300:
                AvgSurvivalTime = '(1200, 1300]'
            elif 1300 < AvgSurvivalTime_val <= 1700:
                AvgSurvivalTime = '(1300, 1700]'
            elif 1700 < AvgSurvivalTime_val:
                AvgSurvivalTime = '>=1700'

            # AvgWalkDistance
            """
            AvgWalkDistance_val = float(instance[AvgWalkDistance_index])
            if AvgWalkDistance_val <= 700:
                AvgWalkDistance = '<=700'
            elif 700 < AvgWalkDistance_val <= 900:
                AvgWalkDistance = '(700, 900]'
            elif 900 < AvgWalkDistance_val <= 1100:
                AvgWalkDistance = '(900, 1100]'
            elif 1100 < AvgWalkDistance_val <= 1300:
                AvgWalkDistance = '(1100, 1300]'
            elif 1300 < AvgWalkDistance_val <= 1450:
                AvgWalkDistance = '(1300, 1450]'
            elif 1450 < AvgWalkDistance_val <= 1600:
                AvgWalkDistance = '(1450, 1600]'
            elif 1600 < AvgWalkDistance_val <= 1800:
                AvgWalkDistance = '(1600, 1800]'
            elif 1800 < AvgWalkDistance_val <= 2200:
                AvgWalkDistance = '(1800, 2200]'
            elif 2200 < AvgWalkDistance_val <= 2700:
                AvgWalkDistance = '(2200, 2700]'
            elif 2700 < AvgWalkDistance_val <= 3500:
                AvgWalkDistance = '(2700, 3500]'
            elif 3500 < AvgWalkDistance_val:
                AvgWalkDistance = '>=3500'
            """

            processed_data.append(
                [
                    instance[player_index],
                    killDeathRatio,
                    damagePg,
                    AvgSurvivalTime,
                    winRatio,
                ])
        return processed_data

    def findProbClassGivenEvidence(self, instance):
        probSet = {}
        for class_val in winRatioRange:
            classPlist = []
            numClassInst = self.calNumClassInstan(class_val)

            for attr_val in instance:
                index = instance.index(attr_val)
                attr = attributes[index]
                num_val_inst = self.calNumAttrGivenClass(attr_val, index, class_val)

                #correct case with zero-frequency
                numerator = float(num_val_inst) + 1.0
                denominator = float(numClassInst) + float(num_attribute_values[attr])
                classPlist.append(numerator/denominator)


            #multiply probabilities together
            all_probs = reduce(lambda x, y: x*y, classPlist)
            class_prob = (float(numClassInst) + 1)/(len(self.trainingDataaaa))
            temp_prob = all_probs * class_prob
            probSet.update({class_val: temp_prob})

        #calculate probabilities for all winRatioRange
        prob_sum = sum(probSet.values())
        for key, value in probSet.iteritems():
            final_prob = value/prob_sum
            final_prob *= 100
            probSet[key] = final_prob
        return probSet

    def calNumClassInstan(self, class_value):
        #count the number of instance of a class value
        num_inst_of_class = 0
        for inst in self.trainingDataaaa[1:]:
            if inst[-1] == class_value:
                num_inst_of_class += 1
        return num_inst_of_class

    def calNumAttrGivenClass(self, value, index, class_value):
        #count the number of instances contain the value
        num_value_in_class = 0
        for inst in self.trainingDataaaa:
            class_present = inst[-1] == class_value
            value_present = inst[index] == value
            if class_present and value_present:
                num_value_in_class += 1
        return num_value_in_class

        
        
        
        
        
        
        