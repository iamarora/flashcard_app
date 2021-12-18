from rest_framework import views, status
from rest_framework.response import Response

from djangoapp.models import Words


class FetchNextWord(views.APIView):

    def get(self, request):
        word_obj = Words()
        return Response(word_obj.get_next_word())


class UpdateWord(views.APIView):

    def put(self, request):
        try:
            word_obj = Words.objects.get(id=request.data['id'])
        except Words.DoesNotExist:
            return Response({"error": "word not found."}, status=status.HTTP_404_NOT_FOUND)
        if request.data['status']:
            word_obj.mark_as_correct()
        else:
            word_obj.mark_as_wrong()
        return Response({"status": "ok"}, status=status.HTTP_202_ACCEPTED)
