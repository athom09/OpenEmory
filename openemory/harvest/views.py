from django.shortcuts import render

from openemory.accounts.auth import permission_required
from openemory.harvest.models import HarvestRecord

@permission_required('harvest.view_harvestrecord')
def queue(request):
    '''Display the queue of harvested records. '''

    # for now, return all records - no pagination, etc.
    # - restrict to only harvested records (which can be ingested or ignored)
    records = HarvestRecord.objects.filter(status='harvested').order_by('harvested').all()
    
    return render(request, 'harvest/queue.html',
                  {'records': records})
