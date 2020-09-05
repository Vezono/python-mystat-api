import requests


class Api:
    def __init__(self):
        self.api_url = 'https://msapi.itstep.org/api/v2'
        self.application_key = '6a56a5df2667e65aab73ce76d1dd737f7d1faef9c52e8b8c55ac75f565d8e8a6'

        self.user_credentials = dict()

    def api_get_request(self, method):
        response = requests.get(f'{self.api_url}{method}',
                                headers={'Authorization': f'Bearer {self.access_token}'})
        return response.json()

    @property
    def access_token(self):
        return self.user_credentials['access_token']

    @property
    def all_cities(self):
        method = '/public/cities'
        response = requests.get(f'{self.api_url}{method}')
        return response.json()

    @property
    def all_languages(self):
        method = '/public/languages'
        response = requests.get(f'{self.api_url}{method}')
        return response.json()

    def translation(self, lang=None):
        """
        :param lang: you can get langs from all_languages
        :return:
        """
        method = '/public/translations'
        response = requests.get(f'{self.api_url}{method}', params={'language': lang})
        return response.json()

    def login(self, username, password) -> requests.request:
        method = '/auth/login'
        response = requests.post(f'{self.api_url}{method}',
                                 data={'username': username,
                                       'password': password,
                                       'application_key': self.application_key}
                                 )
        self.user_credentials = response.json()
        return response

    @property
    def student_achievements(self):
        method = '/profile/statistic/student-achievements'
        response = requests.get(f'{self.api_url}{method}', headers={'Authorization': f'Bearer {self.access_token}'})
        return response.json()

    def materials_list(self, material_type):
        method = '/library/operations/list'
        response = requests.get(f'{self.api_url}{method}',
                                headers={'Authorization': f'Bearer {self.access_token}'},
                                params={'material_type': material_type})
        return response.json()

    @property
    def leader_group_points(self):
        method = '/dashboard/progress/leader-group-points'
        return self.api_get_request(method)

    @property
    def leader_group(self):
        method = '/dashboard/progress/leader-group'
        return self.api_get_request(method)

    @property
    def leader_stream_points(self):
        method = '/dashboard/progress/leader-stream-points'
        return self.api_get_request(method)

    @property
    def leader_stream(self):
        method = '/dashboard/progress/leader-stream'
        return self.api_get_request(method)

    @property
    def study_activity_log(self):
        method = '/dashboard/progress/activity'
        return self.api_get_request(method)

    @property
    def counter_homework(self):
        method = '/count/homework'
        return self.api_get_request(method)

    @property
    def average_progress_chart(self):
        method = '/dashboard/chart/average-progress'
        return self.api_get_request(method)

    @property
    def attendance_chart(self):
        method = '/dashboard/chart/attendance'
        return self.api_get_request(method)

    @property
    def future_exams(self):
        method = '/dashboard/info/future-exams'
        return self.api_get_request(method)

    @property
    def user_info(self):
        method = '/settings/user-info'
        return self.api_get_request(method)

    @property
    def evaluation_list(self):
        method = '/feedback/students/evaluate-lesson-list'
        return self.api_get_request(method)

    @property
    def city_contacts(self):
        method = '/contacts/operations/index'
        return self.api_get_request(method)

    @property
    def student_visits(self):
        method = '/progress/operations/student-visits'
        return self.api_get_request(method)

    @property
    def exams(self):
        method = '/progress/operations/student-exams'
        return self.api_get_request(method)

    @property
    def study_plan_url(self):
        method = '/progress/operations/plan-url'
        return self.api_get_request(method)

    @property
    def progress_chart(self):
        method = '/dashboard/chart/progress'
        return self.api_get_request(method)

    @property
    def history_specs(self):
        method = '/settings/history-specs'
        return self.api_get_request(method)

    @property
    def group_specs(self):
        method = '/settings/group-specs'
        return self.api_get_request(method)

    @property
    def group_history(self):
        method = '/homework/settings/group-history'
        return self.api_get_request(method)

    @property
    def homework_list(self):
        method = '/homework/operations/list'
        return self.api_get_request(method)

    def schedule_month(self, date_filter=None):
        method = '/schedule/operations/get-month'
        response = requests.get(f'{self.api_url}{method}',
                                headers={'Authorization': f'Bearer {self.access_token}'},
                                params={'date_filter': date_filter})
        return response.json()

    def schedule_date(self, date_filter=None):
        method = '/schedule/operations/get-by-date'
        response = requests.get(f'{self.api_url}{method}',
                                headers={'Authorization': f'Bearer {self.access_token}'},
                                params={'date_filter': date_filter})
        return response.json()

    def month_events(self, date_filter=None):
        method = '/schedule/operations/month-events'
        response = requests.get(f'{self.api_url}{method}',
                                headers={'Authorization': f'Bearer {self.access_token}'},
                                params={'date_filter': date_filter})
        return response.json()

    def products_list(self, page=1, product_type=0):
        method = '/market/customer/product/list'
        response = requests.get(f'{self.api_url}{method}',
                                headers={'Authorization': f'Bearer {self.access_token}'},
                                params={'page': page, 'type': product_type})
        return response.json()

    def pushchased_list(self, page=1, product_type=0):
        method = '/market/customer/order/list'
        response = requests.get(f'{self.api_url}{method}',
                                headers={'Authorization': f'Bearer {self.access_token}'},
                                params={'page': page, 'type': product_type})
        return response.json()

    def pushchased_info(self, product_id=0):
        method = '/market/customer/order/info'
        response = requests.get(f'{self.api_url}{method}',
                                headers={'Authorization': f'Bearer {self.access_token}'},
                                params={'id': product_id})
        return response.json()

    @property
    def signal_problems_list(self):
        method = '/signal/operations/problems-list'
        return self.api_get_request(method)

    @property
    def signals_list(self):
        method = '/signal/operations/signals-list'
        return self.api_get_request(method)

    def signals_comments(self, signal_id=0):
        method = '/signal/operations/signals-comments'
        response = requests.get(f'{self.api_url}{method}',
                                headers={'Authorization': f'Bearer {self.access_token}'},
                                params={'id': signal_id})
        return response.json()

    @property
    def unread_signals(self):
        method = '/signal/operations/count-unread'
        return self.api_get_request(method)

    def signal_reference_data(self, reference_type=0):
        method = '/signal/operations/get-reference-data'
        response = requests.get(f'{self.api_url}{method}',
                                headers={'Authorization': f'Bearer {self.access_token}'},
                                params={'type': reference_type})
        return response.json()

    @property
    def signal_reference_status(self):
        method = '/signal/operations/get-reference-status'
        response = requests.get(f'{self.api_url}{method}',
                                headers={'Authorization': f'Bearer {self.access_token}'})
        return response.text

    @property
    def student_itstep_feedbacks(self):
        method = '/feedback/social-review/get-review-list'
        response = requests.get(f'{self.api_url}{method}', headers={'Authorization': f'Bearer {self.access_token}'})
        return response.json()

    @property
    def itstep_reviewing_instruction(self):
        method = '/reviews/index/instruction'
        response = requests.get(f'{self.api_url}{method}', headers={'Authorization': f'Bearer {self.access_token}'})
        return response.json()

    @property
    def profile_data(self):
        method = '/profile/operations/settings'
        response = requests.get(f'{self.api_url}{method}', headers={'Authorization': f'Bearer {self.access_token}'})
        return response.json()

    def send_sms(self):
        method = '/contacts/sms/send-code'
        response = requests.post(f'{self.api_url}{method}', headers={'Authorization': f'Bearer {self.access_token}'})
        return response.json()

    @property
    def recomendations_list(self):
        method = '/referral/operations/list'
        response = requests.get(f'{self.api_url}{method}', headers={'Authorization': f'Bearer {self.access_token}'})
        return response.json()

    @property
    def payment_info(self):
        method = '/payment/operations/index'
        response = requests.get(f'{self.api_url}{method}', headers={'Authorization': f'Bearer {self.access_token}'})
        return response.json()

    @property
    def payment_plan(self):
        method = '/payment/operations/schedule'
        response = requests.get(f'{self.api_url}{method}', headers={'Authorization': f'Bearer {self.access_token}'})
        return response.json()

    @property
    def payment_history(self):
        method = '/payment/operations/history'
        response = requests.get(f'{self.api_url}{method}', headers={'Authorization': f'Bearer {self.access_token}'})
        return response.json()

    @property
    def opened_interview(self):
        method = '/library/quiz/opened-interview'
        response = requests.get(f'{self.api_url}{method}', headers={'Authorization': f'Bearer {self.access_token}'})
        return response.text

    @property
    def latest_news(self):
        method = '/news/operations/latest-news'
        response = requests.get(f'{self.api_url}{method}', headers={'Authorization': f'Bearer {self.access_token}'})
        return response.text

    def news_info(self, news_id=0):
        method = '/news/operations/detail-news'
        response = requests.get(f'{self.api_url}{method}',
                                headers={'Authorization': f'Bearer {self.access_token}'},
                                params={'news_id': news_id})
        return response.json()

    @property
    def unread_news(self):
        method = '/news/operations/count-unread'
        return self.api_get_request(method)
