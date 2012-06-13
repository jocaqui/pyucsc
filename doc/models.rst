.. _models: 

************
Table Models
************

The model objects are automatically loaded from the database and populated with the 
attributes from the table.  A `KnownGene` object will therefore have a 
`txStart`, `txEnd`, etc attributes.  The mapping from database tables to 
objects is performed by SqlAlchemy for us but to query the tables you need to use 
the `SqlAlchemy ORM interface`_

.. _`SqlAlchemy ORM interface`: http://docs.sqlalchemy.org/en/rel_0_7/orm/tutorial.html#querying

Below we list the model methods we have added to the basic data. To find the
attributes belonging to each class, you can use the UCSC table browser's 
`describe table schema` button on the `Table Browser`_

.. _Table Browser: http://genome.ucsc.edu/cgi-bin/hgTables


.. automodule:: ucsc.model
   :members:
   :show-inheritance:
   :inherited-members:
