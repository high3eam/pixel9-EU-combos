import sys
import re

def process_file(input_path, output_path):
    try:
        with open(input_path, 'r') as file:
            lines = file.readlines()

        output_lines = []
        current_block = []
        in_combogroups = False
        brace_count = 0
        removed_count = 0

        for line in lines:
            if line.strip() == 'comboGroups {':
                in_combogroups = True
                current_block = [line]
                brace_count = 1
                continue

            if in_combogroups:
                current_block.append(line)
                brace_count += line.count('{')
                brace_count -= line.count('}')
                
                if brace_count == 0:
                    block_text = ''.join(current_block)
                    bands = [int(band) for band in re.findall(r'band:\s*(\d+)', block_text)]
                    
                    # Check for all forbidden band combinations
                    should_remove = (
                        (3 in bands and 10003 in bands) or
                        (1 in bands and 10001 in bands) or
                        (7 in bands and 10007 in bands)
                    )
                    
                    if not should_remove:
                        output_lines.extend(current_block)
                    else:
                        removed_count += 1
                        
                    in_combogroups = False
                    current_block = []
            else:
                output_lines.append(line)

        with open(output_path, 'w') as file:
            file.writelines(output_lines)
            
        print(f"Removed {removed_count} combo groups.")
        
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file_path> <output_file_path>")
        sys.exit(1)
    
    if sys.argv[1] == sys.argv[2]:
        print("Error: Input and output paths must be different")
        sys.exit(1)
        
    process_file(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()