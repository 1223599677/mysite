from django.shortcuts import render
from django.shortcuts import redirect

from .forms import PrivateGenomeForm
from .models import PrivateGenome


def user_center(request):
    if not request.user.is_authenticated():
        return redirect('users_login')

    form = PrivateGenomeForm()
    private_genome_count = PrivateGenome.objects.filter(
        owner=request.user).count()

    if request.method == 'POST':
        form = PrivateGenomeForm(request.POST, request.FILES)
        if form.is_valid():
            print request.FILES
            private_genome = PrivateGenome(
                    name=form.cleaned_data.get('name',''),
                    document_file=request.FILES.get('document_file', None),
                    sequence_file=request.FILES['sequence_file'],
                    annotation_file=request.FILES['annotation_file'])
            private_genome.owner = request.user
            private_genome.save()
            return render(request, 'utils/upload_success.html')

    return render(request, 'utils/user_center.html', {
            'form': form,
            'private_genome_count': private_genome_count}
        )
