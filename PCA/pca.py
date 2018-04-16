# code from: https://lazyprogrammer.me/tutorial-principal-components-analysis-pca/
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def mainRun1():
    print("mainRun 1 ")    
    pca = PCA()
    X = np.random.random((100,10)) # generate an N = 100, D = 10 random data matrix
    Z = pca.fit_transform(X)

    # visualize the covariance of Z
    plt.imshow(np.cov(Z.T))
    plt.show()


def mainRun2():
    print("mainRun 2 ")    
    # You can also confirm that QTQ=IQTQ=I.

    QTQ = pca.components_.T.dot(pca.components_)
    plt.imshow(QTQ)
    plt.show()

    print( np.around(QTQ, decimals=2))


if __name__ == '__main__':
    mainRun()


