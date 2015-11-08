from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .forms import PrivateGenomeForm
from .models import PrivateGenome
import os


def change_private_genome(request):
    if request.method == 'POST':
        pg_id = request.POST.get('id')

        pg = PrivateGenome.objects.get(id=pg_id, owner=request.user)
        del_code = request.POST.get('del_code')
        if del_code is None:
            return HttpResponse('do nothing')

        if del_code == '1':
            pg.deleted = True
            pg.save()
            return HttpResponse('deleted')
        elif del_code == '0':
            pg.deleted = False
            pg.save()
            return HttpResponse('undeleted')
        else:
            return HttpResponse('del code is wrong')




def user_center(request):
    if not request.user.is_authenticated():
        return redirect('users_login')

    form = PrivateGenomeForm()

    if request.method == 'POST':
        form = PrivateGenomeForm(request.POST, request.FILES)
        if form.is_valid():
            print request.FILES
            private_genome = PrivateGenome(
                name=form.cleaned_data.get('name', ''),
                document_file=request.FILES.get('document_file', None),
                sequence_file=request.FILES['sequence_file'],
                annotation_file=request.FILES['annotation_file'])
            private_genome.owner = request.user
            private_genome.save()
            # call
            os.chdir('/home/qnhu/genebrowser/jbrowse/data/update')
            command = 'nohup bash update.sh {seq} {ann} {usr} {name}_{rstr} {name} &'.format(
                ann = private_genome.annotation_file.path,
                seq = private_genome.sequence_file.path,
                usr = private_genome.owner.username.replace(' ', '_'),
                name = private_genome.get_name(),
                rstr = private_genome.get_random_string()
            )
            print command
            os.popen(command)

            return render(request, 'utils/upload_success.html')

    private_genomes = PrivateGenome.objects.filter(
        owner=request.user, deleted=False)
    return render(request, 'utils/user_center.html', {
            'form': form,
            'private_genomes': private_genomes,
            'private_genome_count': private_genomes.count()}
        )
