#!/usr/bin/env python3
"""
Simple test script to verify XFeat installation.
Run this script after installation to ensure everything is working correctly.
"""

import sys

def test_imports():
    """Test that all required modules can be imported."""
    print("Testing imports...")
    try:
        import torch
        print("✓ PyTorch imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import PyTorch: {e}")
        return False
    
    try:
        import cv2
        print("✓ OpenCV imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import OpenCV: {e}")
        return False
    
    try:
        import kornia
        print("✓ Kornia imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import Kornia: {e}")
        return False
    
    try:
        from modules.xfeat import XFeat
        print("✓ XFeat imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import XFeat: {e}")
        return False
    
    return True

def test_xfeat_initialization():
    """Test XFeat model initialization."""
    print("\nTesting XFeat initialization...")
    try:
        from modules.xfeat import XFeat
        import torch
        
        xfeat = XFeat()
        print("✓ XFeat model initialized successfully")
        
        # Test with a dummy image
        print("\nTesting inference with dummy image...")
        dummy_image = torch.randn(1, 3, 480, 640)
        output = xfeat.detectAndCompute(dummy_image, top_k=100)[0]
        
        print(f"✓ Inference successful!")
        print(f"  - Detected {len(output['keypoints'])} keypoints")
        print(f"  - Descriptor shape: {output['descriptors'].shape if 'descriptors' in output else 'N/A'}")
        
        return True
    except Exception as e:
        print(f"✗ Failed to initialize or run XFeat: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests."""
    print("=" * 60)
    print("XFeat Installation Test")
    print("=" * 60)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed!")
        print("Please ensure all dependencies are installed correctly.")
        sys.exit(1)
    
    # Test XFeat initialization
    if not test_xfeat_initialization():
        print("\n❌ XFeat initialization tests failed!")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✅ All tests passed! XFeat is installed correctly.")
    print("=" * 60)
    print("\nYou can now use XFeat in your projects!")
    print("\nExample usage:")
    print("  from modules.xfeat import XFeat")
    print("  xfeat = XFeat()")
    print("  output = xfeat.detectAndCompute(image, top_k=4096)")

if __name__ == "__main__":
    main()

