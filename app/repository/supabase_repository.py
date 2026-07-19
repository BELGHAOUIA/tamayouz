class Supabase():
    def fetch_data(table,cols,filter,supabase):
       return ( 
        supabase.table(table)
        .select(cols)
        .eq(filter)
        .execute() 
        )

    def insert_data(table,dict,supabase):
        return (
            supabase.table(table)
            .insert(dict)
            .execute()
        )

    def update_data(table,dict,id,supabase):
        return (
            supabase.table(table)
            .update(dict)
            .eq("id", id)
            .execute()
        )

    def delete_data(table,id,supabase):
        return (
            supabase.table(table)
            .delete()
            .eq("id", id)
            .execute()
        )

    def match_data(table,cols,dict,supabase):
        return (
            supabase.table(table)
            .select(cols)
            .match(dict)
            .execute()
        )

    def order_data(table,cols,col_order,supabase):
        return (
            supabase.table(table)
            .select(cols)
            .order(col_order, desc=True)
            .execute()
        )

    def sign_up(dict):
        return (
            supabase.auth.sign_up(dict)
        )

    def sign_in(dict):
        return (
             supabase.auth.sign_in_with_password(dict)
        )

    def sign_out():
        return (
             supabase.auth.sign_out()
        )

    def custom_func(func,supabase):
        return (
            supabase.rpc(func)
            .execute()
        )
    
    
    
