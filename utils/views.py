from django.shortcuts import render
from django.shortcuts import redirect

from .forms import PrivateGenomeForm
from .models import PrivateGenome


def user_center(request):
    if not request.user.is_authenticated():
        return redirect('users_login')

    if request.method == 'POST':
        form = PrivateGenomeForm(request.POST, request.FILES)
        if form.is_valid():
            private_genome = PrivateGenome(
                    sequence_file=request.FILES['sequence_file'],
                    annotation_file=request.FILES['annotation_file'])
            private_genome.owner = request.user
            private_genome.save()
        return render(request, 'utils/upload_success.html')
    else:
        form = PrivateGenomeForm()
        private_genome_count = PrivateGenome.objects.filter(
            owner=request.user).count()

    return render(request, 'utils/user_center.html', {
            'form': form,
            'private_genome_count': private_genome_count}
        )
