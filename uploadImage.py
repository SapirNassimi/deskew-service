import boto3
import datetime



def saveImageToAmazon():
    bucketName = "hesbonit"
    key = "deskewd.jpg"
    outPutname = "deskewd" + str(datetime.datetime.now()) + ".jpeg"

    try:
        s3 = boto3.client('s3')
        s3.upload_file(key, bucketName, outPutname, ExtraArgs={'ACL':'public-read'})

        print("image uploaded successfully to Amazon")

        return '%s/%s/%s' % (s3.meta.endpoint_url, bucketName, key)
    except:
        print("couldnt upload image to Amazon")


#, extra_args={'ACL': 'public-read'}