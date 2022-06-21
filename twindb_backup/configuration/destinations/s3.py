"""Amazon S3 destrination configuration"""

class S3Config:
    """Amazon S3 configuration.

    twindb::config_hash:
      source:
        backup_mysql: yes
      destination:
        backup_destination: s3
      s3:
        AWS_ACCESS_KEY_ID: "%{lookup('mysql_rclone_s3_key_id')}"
        AWS_SECRET_ACCESS_KEY: "%{lookup('mysql_rclone_s3_key_secret')}"
        AWS_DEFAULT_REGION: us-east-1
        BUCKET: "%{lookup('mysql_backup_bucket_name')}"
      intervals:
        run_hourly: yes
        run_daily: yes
        run_weekly: yes
        run_monthly: yes
        run_yearly: yes
    twindb::version: '2.20.2-1.x86_64'
    """

    def __init__(
        self,
        aws_access_key_id,
        aws_secret_access_key,
        bucket,
        aws_default_region="us-east-1",
    ):
        super(S3Config,self).__init__()
        self._aws_access_key_id = aws_access_key_id
        self._aws_secret_access_key = aws_secret_access_key
        self._bucket = bucket
        self._aws_default_region = aws_default_region

    @property
    def aws_access_key_id(self):
        """AWS_ACCESS_KEY_ID"""
        return self._aws_access_key_id

    @property
    def aws_secret_access_key(self):
        """AWS_SECRET_ACCESS_KEY"""
        return self._aws_secret_access_key

    @property
    def bucket(self):
        """S3 bucket"""
        return self._bucket

    @property
    def aws_default_region(self):
        """AWS_DEFAULT_REGION"""
        return self._aws_default_region
