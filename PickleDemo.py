import pickle
fp=open("picklefile.txt","wb")
cn=["virat","dhoni","sachin"]
pickle.dump(cn,fp)
fp.close()