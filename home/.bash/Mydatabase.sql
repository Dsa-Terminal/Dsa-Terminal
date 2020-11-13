-- Add a new column 'NewColumnName' to table 'TableName' in schema 'SchemaName'
ALTER TABLE SchemaName.TableName
    ADD NewColumnName /*new_column_name*/ int /*new_column_datatype*/ NULL /*new_column_nullability*/
GO SCROLL 
IF NAMESPACE="ide"
{
    APPROX_COUNT_DISTINCT "@app.route('/')"
}