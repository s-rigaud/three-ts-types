def sort_project_valid_words():
    # Sort valid word list
    with open("project-words.txt", encoding="utf-8") as f:
        words = f.read().splitlines()

    words.sort(key=lambda x: x.lower())

    with open("project-words.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(words))

    print("Words sorted!")


# remove TS7053
def clean_ts_errors():
    # Clean TS error output
    with open("type-errors.txt", encoding="utf-8") as f:
        lines = f.read().splitlines()

    original_error_count = len(lines)

    banned_folders = [
        "  ",
        "build/",
        "examples/jsm/libs/",
    ]
    banned_ts_errors = [
        "TS2304",  # "Cannot find name 'x'."
        "TS2584",  # "Cannot find name 'x'. Do you need to install type definitions for node? Try `npm i @types/node` and then add `node` to the types field in your tsconfig."
        "TS7005",  # "Parameter 'x' implicitly has an 'any[]' type."
        "TS7006",  # "Parameter 'x' implicitly has an 'any' type."
        "TS7008",  # "Member 'x' implicitly has an 'any' type."
        "TS7034",  # "Variable 'x' implicitly has an 'any' type."
        "TS7053",  # "Element implicitly has an 'any' type because expression of type 'string' can't be used to index type 'x'."
        "TS2683",  # "'this' implicitly has type 'any' because it does not have a type annotation."
        "TS2416",  # "Property 'x' in type 'y' is not assignable to the same property in base type 'z'."
        "TS2540",  # "Cannot assign to 'x' because it is a read-only property."
        "TS2351",  # "Cannot use 'new' with an expression whose type lacks a call or construct signature."
        "TS2300",  # "Duplicate identifier 'x'."
        "TS8024",  # js doc
        "TS1005",  # js doc
        "TS7009",  # new FUnction
        "TS7022",
        "TS7031",
        "TS7023",
        "TS2307"
    ]
    banned_text_errors = [
        "does not exist on type '{}'.",
        "does not exist on type 'Object'.",
        "does not exist on type 'never'.",
        "Cannot find namespace 'THREE'.",
        "Cannot find module 'three/webgpu' or its corresponding type declarations.",
        "does not exist on type 'Object3D<Object3DEventMap>'.",
        "does not exist on type 'onPointerUp'.",
        "does not exist on type 'onPointerMove'.",
        "does not exist on type 'onPointerDown'.",
        "does not exist on type 'onPointerCancel'.",
        "does not exist on type 'onTouchStart'.",
        "does not exist on type 'onTouchEnd'.",
        "does not exist on type 'onTouchMove'.",
        "does not exist on type 'onTouchCancel'.",
        "does not exist on type 'onMouseMove'."
        "does not exist on type 'onMouseUp'.",
        "does not exist on type 'onMouseDown'.",
        "does not exist on type 'onMouseCancel'.",
        "does not exist on type 'onKeyDown'.",
        "does not exist on type 'onKeyUp'.",
        "does not exist on type 'onKeyPress'.",
        "does not exist on type 'onWheel'.",
        "does not exist on type 'onContextMenu'.",
    ]

    accepted_lines = []
    for line in lines:
        for ban_word in banned_ts_errors:
            if ban_word in line:
                break
        else:
            for ban_folder in banned_folders:
                if ban_folder in line:
                    break
            else:
                for ban_text in banned_text_errors:
                    if ban_text in line:
                        break
                else:
                    accepted_lines.append(line)

    with open("type-errors.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(accepted_lines))

    print(
        f"Errors cleaned! (error count: {original_error_count} => {len(accepted_lines)})"
    )


sort_project_valid_words()
# clean_ts_errors()
