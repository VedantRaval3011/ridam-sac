
from flask import Flask, jsonify, request
from flask_cors import CORS
from primary_db import insert_data, get_data, update

app = Flask(__name__)
CORS(app)



@app.route('/view', methods=['GET'])
def get_all():
    rows,fields = get_data()
    if rows:
        result = []
        for row in rows:
            row_data = {}
            for i, column_name in enumerate(fields):
                row_data[column_name.name] = row[i]
            result.append(row_data)
        return jsonify(result)
    else:
        return jsonify({'error': 'Failed to fetch data'})
    
  
@app.route('/update/<id>', methods=['POST'])  
def update_data(id):
    new_name = request.json.get('name')
    new_source_location = request.json.get('source_location')
    new_metadata = request.json.get('metadata')

    if update(id,new_name,new_source_location,new_metadata):
        return jsonify({'message':'Data updated successfully'})
    else:
        return jsonify({'error':'Failed to update data'})


@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json

    id = data.get("id")
    name = data.get("name")
    source_location = data.get("source_location")
    metadata = data.get("metadata")
    temporal_frequency = data.get("temporal_frequency")
    extension = data.get('extension')
    compression = data.get('compression')
    resampling = data.get('resampling')
    interleave = data.get("interleave")
    band_info = data.get('band_info')
    projection = data.get('projection')
    paused = data.get('paused')

    success = insert_data(name, metadata, id, source_location, temporal_frequency, extension, resampling, compression, interleave, projection, paused, band_info) 
    
    if success:
        return jsonify({'message': 'Data added successfully'})
    else:
        return jsonify({'error': 'Failed to add data'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8001)