from string import punctuation

def solution(new_id):
    #1
    new_id = new_id.lower()
    #2
    symbols = punctuation
    symbols  = symbols.replace('-', '').replace('_', '').replace('.', '')
    
    for symbol in symbols:
        new_id = new_id.replace(symbol, '')
    #3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    #4
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    #5  
    if not new_id:
        new_id = 'a'
    #6    
    if len(new_id) > 15:
        new_id = new_id[:15].rstrip('.')
    #7    
    while len(new_id) < 3:
        new_id += new_id[-1]
        
    return new_id