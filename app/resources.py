from import_export import resources
from django.http import HttpResponse
#from django.http import HttpResponse, Http404,response
from .models import *
import pandas as pd
#import sys;
#from twilio.rest import Client



class MemberResource(resources.ModelResource):
    class Meta:
        model = Member
        skip_unchanged= True
        


        

#exporting files 
class ExportFile:
    def exportCSV(rsc, fln):
        file_resource = rsc
        dataset = file_resource.export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename= {fln}.csv'
        return response
    
    def exportJSON(rsc, fln):
        file_resource = rsc
        dataset = file_resource.export()
        response = HttpResponse(dataset.json, content_type='application/json')
        response['Content-Disposition'] = f'attachment; filename= {fln}.json'
        return response
    
    def exportEXCEL(rsc, fln):
        file_resource = rsc
        dataset = file_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename= {fln}.xls'
        return response
    


    def queryExport_C(tbl,fln):
        #perform query here
        queryset = tbl.objects.values('name','contact')
        #print(queryset)
        df = pd.DataFrame.from_dict(queryset)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={fln}.csv'
        df.to_csv(response, index=False)
        return response


   