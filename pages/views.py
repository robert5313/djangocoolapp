from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SearchResultsView(TemplateView):
    template_name = 'search_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query')
        # Perform the search logic based on the query
        # Fetch the relevant results from any data source
        # For instance, you can use a list of dictionaries as results
        results = [
            {'title': 'Result 1', 'description': 'Description of result 1.'},
            {'title': 'Result 2', 'description': 'Description of result 2.'},
            {'title': 'Result 3', 'description': 'Description of result 3.'},
        ]
        context['query'] = query
        context['results'] = results
        return context