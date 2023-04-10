import pandas as pd
from arboreto.algo import grnboost2, genie3
from arboreto.utils import load_tf_names
from distributed import Client

def generateInputs(dataset_uri):
    return pd.read_csv(dataset_uri, header=0, index_col=0)

def run(dataset, algo):
    client = Client(processes = False)    

    if algo == 'GENIE3':
        network = genie3(inDF.to_numpy(), client_or_address = client, gene_names = inDF.columns)
        network.to_csv(opts.outFile, index = False, sep = '\t')

    elif algo == 'GRNBoost2':
        network = grnboost2(inDF.to_numpy(), client_or_address = client, gene_names = inDF.columns)
        network.to_csv(opts.outFile, index = False, sep = '\t')

def parseOutput(**kwargs):
    pass
