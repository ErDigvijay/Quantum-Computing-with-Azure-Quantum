import qsharp
import qsharp.azure
from Test import GenerateRandomBits

qsharp.azure.connect(
   resourceId="/subscriptions/673425fc-08d4-48b7-98d5-fee645785160/resourcegroups/FirstQuantum/providers/Microsoft.Quantum/Workspaces/firstCircuit",
   location="East US")
qsharp.azure.target("ionq.simulator")
result = qsharp.azure.execute(GenerateRandomBits, n=3, shots=1000, jobName="Generate three random bits")
print(result)