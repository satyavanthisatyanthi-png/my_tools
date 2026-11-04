def convert_data_format(data, target_format):
    """
    Convert the input data to the specified target format.

    Parameters:
    data (any): The input data to be converted.
    target_format (str): The desired format to convert the data into. 
                         Supported formats: 'json', 'csv', 'xml'.

    Returns:
    any: The converted data in the specified format.

    Raises:
    ValueError: If the target format is not supported.
    """
    if target_format == 'json':
        import json
        return json.dumps(data)
    elif target_format == 'csv':
        import csv
        from io import StringIO
        
        output = StringIO()
        writer = csv.writer(output)
        
        if isinstance(data, list):
            for row in data:
                writer.writerow(row)
        else:
            raise ValueError("Data must be a list of lists for CSV conversion.")
        
        return output.getvalue()
    elif target_format == 'xml':
        import dicttoxml
        return dicttoxml.dicttoxml(data)
    else:
        raise ValueError(f"Unsupported target format: {target_format}")
