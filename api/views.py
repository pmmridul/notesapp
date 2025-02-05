import logging
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

# Set up logging for the views
logger = logging.getLogger('myapp')  # Replace 'myapp' with your desired logger name

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    logger.info("Fetching available routes")
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    logger.info("Routes fetched successfully")
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    logger.info("Fetching all notes")
    notes = Note.objects.all().order_by('-created')
    serializer = NoteSerializer(notes, many=True)
    logger.info(f"Found {len(notes)} notes")
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    logger.info(f"Fetching note with id: {pk}")
    try:
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(note, many=False)
        logger.info(f"Note with id {pk} fetched successfully")
        return Response(serializer.data)
    except Note.DoesNotExist:
        logger.error(f"Note with id {pk} not found")
        return Response({"error": "Note not found"}, status=404)

@api_view(['PUT'])
def updateNote(request, pk):
    logger.info(f"Updating note with id: {pk}")
    try:
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(instance=note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Note with id {pk} updated successfully")
            return Response(serializer.data)
        else:
            logger.error(f"Invalid data provided for note with id {pk}")
            return Response(serializer.errors, status=400)
    except Note.DoesNotExist:
        logger.error(f"Note with id {pk} not found")
        return Response({"error": "Note not found"}, status=404)

@api_view(['DELETE'])
def deleteNote(request, pk):
    logger.info(f"Deleting note with id: {pk}")
    try:
        note = Note.objects.get(id=pk)
        note.delete()
        logger.info(f"Note with id {pk} deleted successfully")
        return Response('Note was deleted!')
    except Note.DoesNotExist:
        logger.error(f"Note with id {pk} not found")
        return Response({"error": "Note not found"}, status=404)

@api_view(['POST'])
def createNote(request):
    logger.info("Creating a new note")
    data = request.data  # Get the request data safely

    # Handle missing 'body' key
    body = data.get('body', None)
    if body is None:
        logger.error("Missing 'body' field in request data")
        return Response({"error": "Missing 'body' field"}, status=400)

    # If 'body' is present, proceed with note creation
    note = Note.objects.create(body=body)
    logger.info(f"Note created successfully with id: {note.id}")
    return Response({"message": "Note created successfully!", "id": note.id})
