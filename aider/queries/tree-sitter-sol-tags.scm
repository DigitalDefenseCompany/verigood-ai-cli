; Contract definitions
(contract_declaration
  name: (identifier) @name.definition.contract
) @definition.contract

; Function definitions
(function_definition
  name: (identifier) @name.definition.function
) @definition.function

; Constructor definitions
(constructor_definition
  name: (identifier) @name.definition.constructor
) @definition.constructor

; Modifier definitions
(modifier_definition
  name: (identifier) @name.definition.modifier
) @definition.modifier

; Struct definitions
(struct_definition
  name: (identifier) @name.definition.struct
) @definition.struct

; Enum definitions
(enum_definition
  name: (identifier) @name.definition.enum
) @definition.enum

; Event definitions
(event_definition
  name: (identifier) @name.definition.event
) @definition.event

; Function calls
(call_expression
  function: (identifier) @name.reference.call
) @reference.call
(call_expression
  function: (member_expression
    property: (property_identifier) @name.reference.call
  )
) @reference.call

; Contract instantiation
(new_expression
  contract_name: (identifier) @name.reference.contract
) @reference.contract

; Struct instantiation
(new_expression
  struct_name: (identifier) @name.reference.struct
) @reference.struct

; Enum member access
(member_access_expression
  member: (identifier) @name.reference.enum
) @reference.enum