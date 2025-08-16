class CreateStudentRecords < ActiveRecord::Migration[7.0]
  def change
    create_table :student_records do |t|
      t.string :first_name
      t.string :last_name
      t.integer :student_number
      t.float :student_mark

      t.timestamps
    end
  end
end
