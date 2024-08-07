import argparse
from src.config import read_properties_file, load_xml_files
from src.parser import resolve_properties
from src.utils import output_properties, log_missing_properties
from src.model import Model

def main(application_properties_file, environment_properties_file, xml_files_directory, output_mode_value):
    # Read properties from files
    application_properties = read_properties_file(application_properties_file)
    environment_properties = read_properties_file(environment_properties_file)
    
    # Initialize the model
    model = Model(xml_files_directory)
    
    # Resolve properties
    resolved_properties, missing_properties = resolve_properties(application_properties, environment_properties, model.xml_files)
    
    # Log missing properties
    if missing_properties:
        log_missing_properties(missing_properties)
    
    # Output the final properties
    output_properties(output_mode_value, resolved_properties)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process properties and XML files.")
    parser.add_argument('application_properties_file', type=str, help=' application properties file')
    parser.add_argument('environment_properties_file', type=str, help='environment properties file')
    parser.add_argument('xml_files_directory', type=str, help='Directory  XML files')
    parser.add_argument('output_mode', type=int, choices=[1, 2], help='Output mode: 1 for console, 2 for file')
    args = parser.parse_args()
    main(args.application_properties_file, args.environment_properties_file, args.xml_files_directory, args.output_mode)
