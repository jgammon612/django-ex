# credit/api.py

class Credit(models.Model):
    name = models.CharField(max_length=50)
    ssn = models.CharField(max_length=9)
    score = models.CharField(max_length=3)
    
def __str__(self):
       return '%s %s' % (self.ssn, self.score)
