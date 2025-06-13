"""
ExampleClass Methods:
- __init__: Initialize a data processor with configuration parameters
- process_data: Process input data and return results
- get_processor: Get the internal processor instance
- close: Close and clean up processor resources
- __enter__, __exit__: Support for context manager pattern
- __del__: Clean up resources during garbage collection
"""

from typing import Dict, Any, Optional
import os


class ExampleClass:
    """
    A simple example class that processes data and manages resources.
    Demonstrates class structure, context management, and resource handling.
    """
    
    def __init__(self, 
                 config_path: Optional[str] = None, 
                 debug_mode: bool = False):
        """
        Initialize a data processor.
        
        Args:
            config_path (str, optional): Path to configuration file.
                                        If None, will use default configuration.
            debug_mode (bool, optional): Whether to enable debug logging.
        """
        self.config_path = config_path or os.environ.get('DEFAULT_CONFIG_PATH', 'config.json')
        self.debug_mode = debug_mode
        self.processor_id = f"processor_{id(self)}"
        self.is_active = True
        
        if self.debug_mode:
            print(f"Initialized processor {self.processor_id} with config: {self.config_path}")
            
    def get_processor(self) -> str:
        """
        Get the processor identifier.
        
        Returns:
            str: The active processor ID
            
        Raises:
            RuntimeError: If the processor has been closed
        """
        if not self.is_active:
            raise RuntimeError("Processor has been closed")
        return self.processor_id
    
    def process_data(self, input_data: str) -> Dict[str, Any]:
        """
        Process the input data and return results.
        
        Args:
            input_data (str): The data to process
            
        Returns:
            dict: {
                "success": bool - Operation success status,
                "message": str - Description of the operation,
                "result": Any - The processed data (if successful)
            }
        """
        if not self.is_active:
            return {
                "success": False,
                "message": "Processor is not active"
            }
            
        try:
            # Simple example processing
            processed = f"Processed by {self.processor_id}: {input_data}"
            
            return {
                "success": True,
                "message": "Data processed successfully",
                "result": processed
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Processing error: {str(e)}"
            }
    
    def close(self) -> Dict[str, Any]:
        """
        Safely close the processor and release resources.
        
        Returns:
            dict: {
                "success": bool - Operation success status,
                "message": str - Detailed description of result
            }
        """
        if not self.is_active:
            return {
                "success": False,
                "message": "Processor was already closed"
            }
            
        try:
            # Simulate cleanup
            if self.debug_mode:
                print(f"Cleaning up processor {self.processor_id}")
                
            self.is_active = False
            return {
                "success": True,
                "message": "Processor closed successfully"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Failed to close processor: {str(e)}"
            }
    
    def __enter__(self):
        """Support for context manager (with statement)"""
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure processor is closed when exiting context"""
        self.close()
        
    def __del__(self):
        """Attempt to clean up resources during garbage collection"""
        if hasattr(self, 'is_active') and self.is_active:
            try:
                self.close()
            except:
                pass


if __name__ == "__main__":
    # Example 1: Basic usage
    processor = ExampleClass(debug_mode=True)
    try:
        # Get the processor ID
        proc_id = processor.get_processor()
        print(f"Using processor: {proc_id}")
        
        # Process some data
        result = processor.process_data("sample data")
        print(f"Processing result: {result}")
    finally:
        # Always close the processor
        processor.close()
    
    # Example 2: Using as a context manager
    with ExampleClass() as proc:
        result = proc.process_data("context manager example")
        print(f"Result with context manager: {result}")
        # Processor will be automatically closed when exiting the with block
