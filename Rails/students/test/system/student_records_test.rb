require "application_system_test_case"

class StudentRecordsTest < ApplicationSystemTestCase
  setup do
    @student_record = student_records(:one)
  end

  test "visiting the index" do
    visit student_records_url
    assert_selector "h1", text: "Student records"
  end

  test "should create student record" do
    visit student_records_url
    click_on "New student record"

    fill_in "First name", with: @student_record.first_name
    fill_in "Last name", with: @student_record.last_name
    fill_in "Student mark", with: @student_record.student_mark
    fill_in "Student number", with: @student_record.student_number
    click_on "Create Student record"

    assert_text "Student record was successfully created"
    click_on "Back"
  end

  test "should update Student record" do
    visit student_record_url(@student_record)
    click_on "Edit this student record", match: :first

    fill_in "First name", with: @student_record.first_name
    fill_in "Last name", with: @student_record.last_name
    fill_in "Student mark", with: @student_record.student_mark
    fill_in "Student number", with: @student_record.student_number
    click_on "Update Student record"

    assert_text "Student record was successfully updated"
    click_on "Back"
  end

  test "should destroy Student record" do
    visit student_record_url(@student_record)
    click_on "Destroy this student record", match: :first

    assert_text "Student record was successfully destroyed"
  end
end
