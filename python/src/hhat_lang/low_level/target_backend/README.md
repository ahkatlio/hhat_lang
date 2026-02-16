# Target Backend Implementations

The `target_backend` directory contains integrations with specific quantum computing platforms, providing the interface layer between H-hat's low-level quantum languages and actual quantum hardware, simulators, and emulators.

## Overview

This module implements backend-specific communication layers that enable H-hat programs to execute on real quantum computers and simulators. Each subdirectory provides integration with a specific quantum computing platform or framework.

## Structure

### Subdirectories

#### `qiskit/`
**Qiskit** (IBM Quantum) backend integration

- **Platform**: IBM Quantum
- **Vendor**: IBM
- **Access**: IBM Quantum Experience, IBM Cloud
- **Simulators**: Aer simulators (statevector, QASM, unitary)
- **Hardware**: IBM Quantum systems (various qubit counts and topologies)

**Capabilities**:
- Submit circuits to IBM Quantum devices
- Run on local Qiskit simulators
- Queue management and job monitoring
- Result retrieval and post-processing
- Noise modeling and error mitigation
- Circuit transpilation and optimization

**Supported Features**:
- Gate-based quantum circuits
- Pulse-level programming (advanced)
- Dynamic circuits
- Classical feedforward
- Mid-circuit measurements

#### `squidasm/`
**SquidASM** (Quantum Network Simulator) backend integration

- **Platform**: Quantum Network Simulation
- **Purpose**: Simulate quantum network protocols
- **Type**: Network simulator
- **Focus**: Distributed quantum computing, quantum internet

**Capabilities**:
- Simulate quantum network topologies
- Model entanglement distribution
- Test quantum communication protocols
- Validate distributed quantum algorithms
- Network performance analysis

**Supported Features**:
- Multi-node quantum systems
- Quantum channel modeling
- Classical communication integration
- Quantum memory simulation
- Imperfect entanglement

## Key Concepts

### Backend Integration

Each backend implements integration with a specific platform:

```python
class QiskitBackend:
    def __init__(self, config):
        """Initialize Qiskit backend"""
        self.provider = QiskitProvider(config)
        self.device = self.provider.get_backend(config['device_name'])
    
    def submit(self, qlang_code: str) -> JobID:
        """Submit quantum circuit for execution"""
        # Parse LLQ code
        # Create Qiskit circuit
        # Submit to device
        # Return job ID
    
    def retrieve(self, job_id: JobID) -> Results:
        """Retrieve execution results"""
        # Query job status
        # Wait for completion
        # Extract results
        # Post-process
        # Return measurement data
```

### Submission Workflow

```
H-hat Program
      ↓
Quantum IR
      ↓
LLQ Translation (OpenQASM/NetQASM)
      ↓
Backend Adapter
      ↓
Platform-Specific Format
      ↓
Backend API
      ↓
Quantum Device/Simulator
      ↓
Execution
      ↓
Measurement Results
      ↓
Backend Adapter
      ↓
H-hat Data Types
```

### Backend Abstraction

Backends provide platform-independent interface:

**Common Operations**:
- **Submit**: Send circuit for execution
- **Monitor**: Check job status
- **Retrieve**: Get execution results
- **Cancel**: Abort running job
- **List Devices**: Query available devices

**Platform-Specific Details Hidden**:
- Authentication mechanisms
- API endpoints and protocols
- Data formats
- Queue systems
- Error handling

### Device Configuration

Backends configured through settings:

```python
qiskit_config = {
    'provider': 'ibm',
    'api_token': 'YOUR_TOKEN',
    'device_name': 'ibmq_manila',  # or 'aer_simulator'
    'shots': 1024,
    'optimization_level': 2,
    'memory': True
}

squidasm_config = {
    'network_topology': 'star',
    'num_nodes': 3,
    'fidelity': 0.95,
    'gate_error_rate': 0.001
}
```

### Job Management

Backends handle asynchronous job execution:

**Job Lifecycle**:
1. **Submit**: Circuit sent to backend → Job ID returned
2. **Queue**: Job enters execution queue
3. **Running**: Device executing circuit
4. **Completed**: Results available
5. **Retrieve**: Fetch and process results

**Status Monitoring**:
```python
job_id = backend.submit(circuit)

while not backend.is_complete(job_id):
    status = backend.get_status(job_id)
    print(f"Job status: {status}")
    time.sleep(1)

results = backend.retrieve(job_id)
```

### Result Processing

Backends format results consistently:

**Raw Results**:
- Bit strings from measurements
- Shot counts (histogram)
- State vectors (simulators)
- Density matrices (noise simulation)

**Processed Results**:
```python
{
    'counts': {
        '00': 512,
        '01': 128,
        '10': 256,
        '11': 128
    },
    'shots': 1024,
    'success': True,
    'execution_time': 2.5,  # seconds
    'metadata': {...}
}
```

## Qiskit Backend Details

### IBM Quantum Integration

**Authentication**:
```python
from qiskit import IBMQ
IBMQ.save_account('YOUR_API_TOKEN')
provider = IBMQ.load_account()
```

**Device Selection**:
```python
# List available devices
devices = provider.backends()

# Get specific device
backend = provider.get_backend('ibmq_manila')

# Device properties
print(backend.configuration())
print(backend.properties())
```

**Circuit Execution**:
```python
from qiskit import QuantumCircuit, execute

# Create circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Execute
job = execute(qc, backend, shots=1024)

# Get results
result = job.result()
counts = result.get_counts()
```

### Local Simulation

**Aer Simulators**:
```python
from qiskit import Aer

# State vector simulator
backend = Aer.get_backend('statevector_simulator')

# QASM simulator
backend = Aer.get_backend('qasm_simulator')

# Unitary simulator
backend = Aer.get_backend('unitary_simulator')
```

### Noise Modeling

```python
from qiskit.providers.aer.noise import NoiseModel

# Get noise model from real device
noise_model = NoiseModel.from_backend(ibmq_device)

# Use in simulation
job = execute(qc, aer_backend, noise_model=noise_model)
```

## SquidASM Backend Details

### Network Configuration

**Topology Setup**:
```python
network_config = {
    'nodes': ['alice', 'bob', 'charlie'],
    'links': [
        {'source': 'alice', 'target': 'bob', 'fidelity': 0.95},
        {'source': 'bob', 'target': 'charlie', 'fidelity': 0.92}
    ]
}
```

**Node Programming**:
```python
# Alice's node program
def alice_program(node):
    # Create EPR pair with Bob
    epr = node.create_epr('bob')
    
    # Perform local operations
    node.apply_gate('H', epr)
    
    # Measure
    result = node.measure(epr)
    return result
```

### Distributed Execution

**Multi-Node Simulation**:
```python
network = SquidASMNetwork(config)

# Set node programs
network.set_program('alice', alice_program)
network.set_program('bob', bob_program)

# Run simulation
results = network.run()

# Extract per-node results
alice_result = results['alice']
bob_result = results['bob']
```

## Connections

- **`low_level/quantum_lang`**: Receives LLQ code for execution
- **`core/execution`**: Backend invoked during quantum program execution
- **`core/cast`**: Backend execution triggered by quantum-to-classical cast
- **`core/config`**: Backend configuration from project settings
- **`core/error_handlers`**: Reports backend errors

## Usage Context

Backends are used for:

- **Real Quantum Execution**: Running on actual quantum hardware
- **Simulation**: Testing quantum algorithms
- **Development**: Debugging quantum programs
- **Research**: Exploring quantum algorithms
- **Education**: Learning quantum computing

## Backend Selection

Selection criteria:

**By Device Availability**:
- Check user's access credentials
- Query available devices
- Select based on qubit count, connectivity

**By Program Requirements**:
- Number of qubits needed
- Gate set requirements
- Noise tolerance

**By Performance**:
- Queue time
- Execution speed
- Cost (cloud resources)

**Selection Algorithm**:
```python
def select_backend(requirements):
    available = query_available_backends()
    
    # Filter by requirements
    compatible = filter_compatible(available, requirements)
    
    # Rank by performance
    ranked = rank_by_performance(compatible)
    
    # Return best match
    return ranked[0]
```

## Error Handling

Backends handle various errors:

**Connection Errors**:
- Network failures
- Authentication issues
- API timeouts

**Execution Errors**:
- Invalid circuits
- Resource limits exceeded
- Device errors

**Result Errors**:
- Job failures
- Corrupted data
- Timeout waiting for results

**Error Recovery**:
- Retry logic
- Fallback to simulators
- Clear error messages

## Extension Guidelines

To add a new backend:

1. **Create Subdirectory**:
   ```
   target_backend/
   └── my_backend/
       ├── __init__.py
       ├── backend.py
       ├── adapter.py
       └── utils.py
   ```

2. **Implement Backend Class**:
   ```python
   class MyBackend:
       def __init__(self, config):
           # Initialize platform connection
           pass
       
       def submit(self, qlang_code: str) -> JobID:
           # Submit circuit
           pass
       
       def retrieve(self, job_id: JobID) -> Results:
           # Get results
           pass
   ```

3. **Create Adapter**:
   - Convert LLQ to platform format
   - Transform results to H-hat format

4. **Handle Authentication**:
   - API keys, tokens
   - OAuth flows
   - Credential storage

5. **Implement Job Management**:
   - Submission
   - Status monitoring
   - Result retrieval
   - Cancellation

6. **Test Integration**:
   - Unit tests
   - Integration tests with platform
   - Mock backend for testing

7. **Document**:
   - Setup instructions
   - Configuration options
   - Usage examples
   - Limitations

## Performance Considerations

**Submission Overhead**:
- Minimize API calls
- Batch multiple circuits
- Use caching when appropriate

**Network Latency**:
- Consider cloud vs. local execution
- Use simulators for development
- Reserve hardware for production

**Result Processing**:
- Efficient data parsing
- Minimal post-processing
- Stream large result sets

## Security Considerations

**Credentials**:
- Secure storage of API keys
- No hardcoded credentials
- Environment variables or secure vaults

**Data Privacy**:
- Circuit privacy on cloud platforms
- Result confidentiality
- Compliance with data regulations

**Access Control**:
- User authentication
- Resource quotas
- Usage monitoring

## Future Directions

**Planned Backends**:
- **AWS Braket**: Amazon's quantum service
- **Azure Quantum**: Microsoft's platform
- **Google Quantum**: Cirq integration
- **IonQ**: Trapped ion quantum computers
- **Rigetti**: Quil-based execution
- **D-Wave**: Quantum annealing

**Enhanced Features**:
- **Multi-Backend Execution**: Run on multiple platforms concurrently
- **Backend Pooling**: Automatic backend selection and load balancing
- **Hybrid Execution**: Classical-quantum workload splitting
- **Result Caching**: Store and reuse results
- **Cost Optimization**: Minimize cloud execution costs
- **Quality of Service**: SLA management, priority queuing
