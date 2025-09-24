import os
import torch

def test_cuda_visibility():
    """Test CUDA visibility and GPU access"""
    
    # Check CUDA_VISIBLE_DEVICES environment variable
    cuda_visible = os.environ.get('CUDA_VISIBLE_DEVICES', 'Not set')
    print(f"CUDA_VISIBLE_DEVICES: {cuda_visible}")
    
    # Check PyTorch CUDA availability
    print(f"CUDA available: {torch.cuda.is_available()}")
    
    if torch.cuda.is_available():
        # Get number of visible GPUs
        gpu_count = torch.cuda.device_count()
        print(f"Number of visible GPUs: {gpu_count}")
        
        # List all visible GPUs
        for i in range(gpu_count):
            gpu_name = torch.cuda.get_device_name(i)
            print(f"GPU {i}: {gpu_name}")
            
        # Test tensor creation on GPU
        try:
            device = torch.device('cuda:0')
            test_tensor = torch.tensor([1.0, 2.0, 3.0]).to(device)
            print(f"Successfully created tensor on GPU: {test_tensor.device}")
        except Exception as e:
            print(f"Error creating tensor on GPU: {e}")
    else:
        print("No CUDA GPUs available")

if __name__ == "__main__":
    test_cuda_visibility()