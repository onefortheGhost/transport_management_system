from django.shortcuts import render

class DispatchBoardViewSet(viewsets.ModelViewSet):
    queryset = DispatchBoard.objects.all()
    serializer_class = DispatchBoardSerializer