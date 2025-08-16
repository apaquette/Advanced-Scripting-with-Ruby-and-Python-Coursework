json.extract! student_record, :id, :first_name, :last_name, :student_number, :student_mark, :created_at, :updated_at
json.url student_record_url(student_record, format: :json)
