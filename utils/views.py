# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PrivateGenomeForm, SequenceInfoForm
from .models import PrivateGenome, SequenceInfo
import os


@login_required
def user_center(request):
    return render(request, 'utils/user_center.html')


@login_required
def genome_center(request):
    return render(request, 'utils/genome_center.html')


@login_required
def genome_upload(request):
    form = PrivateGenomeForm()

    if request.method == 'POST':
        private_genome_form = PrivateGenomeForm(request.POST, request.FILES)
        if private_genome_form.is_valid():
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
                ann=private_genome.annotation_file.path,
                seq=private_genome.sequence_file.path,
                usr=private_genome.owner.username.replace(' ', '_'),
                name=private_genome.get_name(),
                rstr=private_genome.get_random_string()
            )
            print command
            os.popen(command)

            return render(request, 'utils/genome_upload_success.html')

    return render(request, 'utils/genome_upload.html', {'form': form})


@login_required
def genome_browser(request):
    print 'browser'
    private_genomes = PrivateGenome.objects.filter(
        owner=request.user, deleted=False)
    return render(request, 'utils/genome_browser.html', {
        'private_genomes': private_genomes,
        'private_genome_count': private_genomes.count()}
    )


@login_required
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


@login_required
def search_sequence_info(request):
    if request.method == 'POST':
        kwargs = {}
        strain = request.POST.get('strain', '').strip()
        application = request.POST.get('application', '').strip()

        if not strain and not application:
            return render(request, 'utils/search_sequence_info.html', {
                'keyword_error': True,
                'err_title': 'Nothing Input',
                'err_content': 'please input at least a keyword!'
            }
            )
        if strain:
            kwargs['strain__icontains'] = strain
        if application:
            kwargs['industrial_application__icontains'] = application

        sequences = SequenceInfo.objects.filter(**kwargs)
        return render(request, 'utils/search_sequence_results.html', {
            'sequences': sequences,
            'strain': strain,
            'application': application,
        })

    else:
        return render(request, 'utils/search_sequence_info.html')


@login_required
def sequence_info_upload(request):
    private_genome = get_object_or_404(PrivateGenome,
        pk=request.GET.get('pk'),
        random_string = request.GET.get('code', '')
    )

    kwargs = {}
    if private_genome.sequence_info:
        instance = private_genome.sequence_info
        kwargs['instance'] = instance
    else:
        instance = SequenceInfo(strain_owner=request.user.real_name)

    form = SequenceInfoForm(**kwargs)

    if request.method == 'POST':
        form = SequenceInfoForm(request.POST, request.FILES, **kwargs)
        if form.is_valid():
            sequence_info = form.save()
            private_genome.sequence_info = sequence_info
            private_genome.save()

            return render(request, 'utils/sequence_info_upload_success.html',
                {'sequence_info': sequence_info})

    return render(request, 'utils/sequence_info_upload.html', {
        'form': form, 'private_genome': private_genome})


@login_required
def sequence_info_detail(request, pk):
    sequence_info = get_object_or_404(SequenceInfo, pk=pk)
    return render(request, 'utils/sequence_info_detail.html', {
                'sequence_info': sequence_info})
