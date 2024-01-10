import pytest

from pages.BasicFormPage import BasicFormPage


class Test:
    test_data_names = 'username, password, comments, filename, hiddenField, checkboxes,\
                        radioval, multipleselect, dropdown, submitbutton'
    test_data = ('testuser', 'testpassword123', 'test comment !@#$%', 'test_resourses/test.json',
                 'Hidden Field Value', 2, 3, 'ms4', 'dd6', 'submit')

    @pytest.mark.parametrize(test_data_names, [test_data])
    def test(self, page, username, password, comments, filename, hiddenField, checkboxes,
             radioval, multipleselect, dropdown, submitbutton):
        p = BasicFormPage(page=page, url='https://testpages.eviltester.com/styled/basic-html-form-test.html')
        p.open()
        p.fill_username(value=username)
        p.fill_password(value=password)
        p.fill_comment(value=comments)
        p.upload_file(path=filename)
        p.uncheck_all_checkboxes()
        p.check_checkbox_by_number(checkbox_number=checkboxes)
        p.click_radio_button(button_number=radioval)
        p.select_option(value=multipleselect)
        p.select_dropdown_option(value=dropdown)
        p.submit_form()
        p.verify_all_data(username, password, comments, filename, hiddenField,
                          checkboxes, radioval, multipleselect, dropdown, submitbutton)

