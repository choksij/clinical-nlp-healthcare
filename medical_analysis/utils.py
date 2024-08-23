import os

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def map_class_id_to_name(class_id):
    class_map = {
        0: 'Class 0: Example Disease A',
        1: 'Class 1: Example Disease B',
        # Add more mappings as needed
    }
    return class_map.get(class_id, f'Unknown Class ID: {class_id}')
