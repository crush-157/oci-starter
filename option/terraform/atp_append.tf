/*
// WALLET
resource "oci_database_autonomous_database_wallet" "autonomous_data_warehouse_wallet" {
  autonomous_database_id = data.oci_database_autonomous_database.starter_atp.id
  password               = "welcome1"
  base64_encode_content  = "true"
}

resource "local_file" "autonomous_data_warehouse_wallet_file" {
  content_base64 = oci_database_autonomous_database_wallet.autonomous_data_warehouse_wallet.content
  filename       = "atp_wallet.zip"
}

// -- OUTPUT ----------------------------------------------------------------

output "autonomous_database_wallet" {
  value = "atp_wallet.zip"
}
*/

locals {
  # Create List of 'name' values from source objet list
  list_profiles = [for v in data.oci_database_autonomous_database.starter_atp.connection_strings[0].profiles : format("%s/%s",v.protocol,v.consumer_group)]
  # Get index for 'name' equal to "Dan"
  index_profile = index(local.list_profiles, "TCPS/MEDIUM")
  db_url = replace(data.oci_database_autonomous_database.starter_atp.connection_strings[0].profiles[local.index_profile].value, " ", "")
  jdbc_url = format("jdbc:oracle:thin:@%s", local.db_url)
  # Create List of 'name' values from source objet list
  ords_url = replace(data.oci_database_autonomous_database.starter_atp.connection_urls[0].apex_url, "ords/apex", "ords" )
}

output "ords_url" {
  value = local.ords_url
}