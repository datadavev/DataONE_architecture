import os, sys, re, glob

apis = {
	# Application
	'app_client' : ('Client', 'Application'),
	'app_admin' : ('Admin', 'Application'),
	
	# Member Node API.
	'm_authorize' : ('Authorization API', 'Member Node'),
	'm_crud' : ('CRUD API', 'Member Node'),
	'm_rep' : ('Replication API', 'Member Node'),
	'm_authenticate' : ('Server Authentication API', 'Member Node'),
	'm_cap' : ('Capabilities API', 'Member Node'),
	'm_health' : ('State of Health API', 'Member Node'),

	'm_authorize_a' : ('Authorization API', 'Member Node A'),
	'm_crud_a' : ('CRUD API', 'Member Node A'),
	'm_rep_a' : ('Replication API', 'Member Node A'),
	'm_authenticate_a' : ('Server Authentication API', 'Member Node A'),
	'm_cap_a' : ('Capabilities API', 'Member Node A'),
	'm_health_a' : ('State of Health API', 'Member Node A'),

	'm_authorize_b' : ('Authorization API', 'Member Node B'),
	'm_crud_b' : ('CRUD API', 'Member Node B'),
	'm_rep_b' : ('Replication API', 'Member Node B'),
	'm_authenticate_b' : ('Server Authentication API', 'Member Node B'),
	'm_cap_b' : ('Capabilities API', 'Member Node B'),
	'm_health_b' : ('State of Health API', 'Member Node B'),

	# Coordinating Node API.
	'c_authenticate' : ('Authentication API', 'Coordinating Node'),
	'c_ver' : ('Verify API', 'Coordinating Node'),
	'c_authorize' : ('Authorization API', 'Coordinating Node'),
	'c_query' : ('Query API', 'Coordinating Node'),
	'c_crud' : ('CRUD API', 'Coordinating Node'),
	'c_rep' : ('Replication API', 'Coordinating Node'),
	'c_sync' : ('Synchronization API', 'Coordinating Node'),
	'c_reg' : ('Register API', 'Coordinating Node'),
	'c_srv_auth' : ('Server Authentication API', 'Coordinating Node'),
	'c_health' : ('State of Health API', 'Coordinating Node'),
}

for ss in glob.glob ('*.interaction'):
	in_file = open (ss, 'r')
	out_file = open ('%s.txt' % ss, 'w')

	out_file.writelines ('@startuml\n')

	# Generate title line from filename.
	path, fname = os.path.split (ss)
	base, ext = os.path.splitext (fname)
	out_file.writelines ('title Interactions %s\n' % base)
	
	print (base)

	out_file.writelines ('autonumber\n')
	out_file.writelines ('skin BlueModern\n')
	
	declared = {}
	
	for line in in_file:
	# Create "participant" entry for line if neccessary.
		for api in apis.keys ():
			m = re.match ('.*%s\W.*' % api, line)
			if m:
				try:
					declared [api]
				except KeyError:
					declared [api] = True
					api_class = ''
					out_file.writelines ('participant "%s" as %s << %s >>\n' % (apis[api][0], api, apis[api][1]))
		# Output line.
		out_file.writelines (line)

	out_file.writelines ('@enduml\n')

