import numpy as np
import matplotlib.pyplot as plt

# Generate coefficients of least-square regression line
def genCoefficient(dataX, dataY, dataW):
    N = np.size(dataX)

    # Check https://ms.mcmaster.ca/canty/teaching/stat3a03/Lectures7.pdf
    weightMeanX = np.mean(dataX * dataW) / np.mean(dataW)
    weightMeanY = np.mean(dataY * dataW) / np.mean(dataW)

    slope = np.sum(dataW * (dataX - weightMeanX) * (dataY - weightMeanY)) / np.sum(dataW * (dataX - weightMeanX) * (dataX - weightMeanX))
    intercept = weightMeanY - slope * weightMeanX

    return [intercept, slope]

# Draw LSRL on plot
def genPlot(dataX, dataY, coef, dataErr):
    N = np.size(dataX)

    plt.xlabel('X Values')
    plt.ylabel('Y Values')

    # Plot points as scatter plot
    plt.scatter(dataX, dataY)

    # Plot LSRL using coefficients
    dataYPred = coef[0] + coef[1] * dataX
    plt.plot(dataX, dataYPred)

    # Draw error bars on the plot

    horizWidthPoints = (plt.axis()[1] - plt.axis()[0]) / N
    horizWidthError = horizWidthPoints / 20

    for i in range(N):
        plt.plot((dataX[i], dataX[i]), (dataY[i] - dataErr[i], dataY[i] + dataErr[i]), color = 'red')

        # Draw horizontal bars at the end of error bars
        plt.plot((dataX[i] - horizWidthError, dataX[i] + horizWidthError), (dataY[i] + dataErr[i], dataY[i] + dataErr[i]), color = 'red')
        plt.plot((dataX[i] - horizWidthError, dataX[i] + horizWidthError), (dataY[i] - dataErr[i], dataY[i] - dataErr[i]), color = 'red')

    plt.show()

def main():
    listX = []
    listY = []
    listErr = []
    listW = []

    with open('data_txt.txt') as f:
        for line in f.readlines():
            curLine = line.strip().split(', ')

            listX.append(float(curLine[0]))
            listY.append(float(curLine[1]))
            listErr.append(float(curLine[2]))
            listW.append(1 / float(curLine[2]))
    
    dataX = np.array(listX)
    dataY = np.array(listY)
    dataErr = np.array(listErr)
    dataW = np.array(listW)

    coef = genCoefficient(dataX, dataY, dataW)
    genPlot(dataX, dataY, coef, dataErr)

main()
