import json
import boto3
import os
import pandas as pd


client = boto3.client('dynamodb')

def importCSVToDB(event, context):
    documentsTable = os.environ['documentsTable']

    df =pd.read_csv('afs_lic_201902.csv', skip_blank_lines=True,
                    usecols=['REGISTER_NAME', 'AFS_LIC_NUM', 'AFS_LIC_NAME', 'AFS_LIC_ADD_LOCAL',
                             'AFS_LIC_ADD_STATE', 'AFS_LIC_ADD_PCODE'])

    df = df.astype(str)
    df = df.fillna("NA")
    values = df.T.to_dict().values()

    for value in values:
        print(value)
        client.update_item(
            TableName=documentsTable,
            Key={
                'string': {
                    value.AFS_LIC_NUM
                }
            },
            AttributeUpdates={
                'string': {
                    'Value': {
                        'S': 'string',
                        'N': 'string',
                        'B': b'bytes',
                        'SS': [
                            'string',
                        ],
                        'NS': [
                            'string',
                        ],
                        'BS': [
                            b'bytes',
                        ],
                        'M': {
                            'string': {'... recursive ...'}
                        },
                        'L': [
                            {'... recursive ...'},
                        ],
                        'NULL': True | False,
                        'BOOL': True | False
                    },
                    'Action': 'ADD' | 'PUT' | 'DELETE'
                }
            },
            Expected={
                'string': {
                    'Value': {
                        'S': 'string',
                        'N': 'string',
                        'B': b'bytes',
                        'SS': [
                            'string',
                        ],
                        'NS': [
                            'string',
                        ],
                        'BS': [
                            b'bytes',
                        ],
                        'M': {
                            'string': {'... recursive ...'}
                        },
                        'L': [
                            {'... recursive ...'},
                        ],
                        'NULL': True | False,
                        'BOOL': True | False
                    },
                    'Exists': True | False,
                    'ComparisonOperator': 'EQ' | 'NE' | 'IN' | 'LE' | 'LT' | 'GE' | 'GT' | 'BETWEEN' | 'NOT_NULL' | 'NULL' | 'CONTAINS' | 'NOT_CONTAINS' | 'BEGINS_WITH',
                    'AttributeValueList': [
                        {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True | False,
                            'BOOL': True | False
                        },
                    ]
                }
            },
            ConditionalOperator='AND' | 'OR',
            ReturnValues='NONE' | 'ALL_OLD' | 'UPDATED_OLD' | 'ALL_NEW' | 'UPDATED_NEW',
            ReturnConsumedCapacity='INDEXES' | 'TOTAL' | 'NONE',
            ReturnItemCollectionMetrics='SIZE' | 'NONE',
            UpdateExpression='string',
            ConditionExpression='string',
            ExpressionAttributeNames={
                'string': 'string'
            },
            ExpressionAttributeValues={
                'string': {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True | False,
                    'BOOL': True | False
                }
            }

    #with pd.option_context('display.max_rows', None, 'display.max_columns', None):


