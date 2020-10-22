# diagram przykładowego wykorzystania Istio w klastrze k8s

from diagrams import Cluster, Diagram
from diagrams.onprem.network import Istio
from diagrams.onprem.database import MongoDB
from diagrams.onprem.queue import Rabbitmq
from diagrams.k8s.ecosystem import Helm
from diagrams.onprem.compute import Server
from diagrams.gcp.compute import AppEngine, Functions
from diagrams.gcp.network import LoadBalancing
from diagrams.gcp.ml import InferenceAPI
from diagrams.gcp.database import Datastore
from diagrams.gcp.compute import Functions

with Diagram("Diagram-Istio", show=False, outformat="png"):
    with Cluster("K8s"): 
        api = InferenceAPI("API k8s")
        
        with Cluster("Istio"):
            ing = Istio("IngressGateway")
            gt = Istio("Gateway")
            vs   = Istio("VirtualService") 
            se = Istio("ServiceEntry")

    db = Datastore("External Database")
    server = InferenceAPI("External API")
    helm = Functions("Helm")
    lb = LoadBalancing("In")

    se << db
    se << server
    helm >> api
    lb >> ing
    api >> ing 
    api >> vs
    api >> se
    api >> gt


