from discount.models import Company, City, Adress, View, SocialNetworks


class CompanyDto:
    def __init__(self, company):
        self.name = company.name
        self.photo = company.photo
        self.description = company.description
        self.discount_percent = company.discount.percent
        self.city = company.adress.city.name
        self.view_count = View.objects.get(company=company).count



def get_company_dto():
    company_list_qureyset = Company.objects.all()
    print(company_list_qureyset)
    list = []
    for comp in company_list_qureyset:
        list.append(CompanyDto(comp))
    return list

class CompanyDetail(CompanyDto):
    def __init__(self, company):
        super().__init__(company)
        self.urls = SocialNetworks.objects.get(company=company).urls
        self.type = SocialNetworks.objects.get(company=company).type
        self.logo = SocialNetworks.objects.get(company=company).logo
        self.adress = company.adress.adress
        self.longitude = company.adress.longitude
        self.latitude = company.adress.latitude
        self.working_hours = company.working_hours



def get_company_detail_dto():
    company_list_qureyset = Company.objects.all()
    print(company_list_qureyset)
    list = []
    for comp in company_list_qureyset:
        list.append(CompanyDetail(comp))
    return list














